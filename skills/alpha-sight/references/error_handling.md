# Error Handling

This document provides comprehensive error handling strategies for the Alpha-Sight skill.

## Table of Contents

- [General Principles](#general-principles)
- [API Errors](#api-errors)
- [File System Errors](#file-system-errors)
- [Execution Errors](#execution-errors)
- [Resource Limit Errors](#resource-limit-errors)
- [Network Errors](#network-errors)
- [Parsing Errors](#parsing-errors)

## General Principles

1. **Fail Gracefully**: Never crash the entire workflow due to a single error
2. **Degrade Functionality**: Continue with reduced features if possible
3. **Log Everything**: Record all errors for debugging and reporting
4. **Inform User**: Provide clear, actionable error messages
5. **Preserve State**: Save progress before failing
6. **Retry Intelligently**: Use exponential backoff for transient errors
7. **Clean Up**: Release resources even when errors occur

## API Errors

### arXiv API Errors

#### Error: Paper Not Found (404)

**Cause**: Invalid arXiv ID or paper doesn't exist

**Detection**:
```python
response = requests.get(f"http://export.arxiv.org/api/query?id_list={arxiv_id}")
if "No entries found" in response.text:
    # Paper not found
```

**Handling**:
```python
print(f"✗ Error: Paper {arxiv_id} not found on arXiv")
print(f"  Please check the arXiv ID and try again")
print(f"  Valid format: YYMM.NNNNN (e.g., 2401.12345)")
sys.exit(1)
```

**User Message**:
```
✗ Error: Paper 2401.99999 not found on arXiv

Please check the arXiv ID and try again.
Valid format: YYMM.NNNNN (e.g., 2401.12345)
```

#### Error: Rate Limit Exceeded (429)

**Cause**: Too many requests to arXiv API (limit: 1 request per 3 seconds)

**Detection**:
```python
if response.status_code == 429:
    # Rate limited
```

**Handling**:
```python
max_retries = 3
for attempt in range(max_retries):
    try:
        response = requests.get(url)
        response.raise_for_status()
        break
    except requests.HTTPError as e:
        if e.response.status_code == 429:
            wait_time = 2 ** attempt * 3  # 3s, 6s, 12s
            print(f"Rate limited. Waiting {wait_time}s before retry {attempt + 1}/{max_retries}...")
            time.sleep(wait_time)
        else:
            raise
else:
    print("✗ Error: arXiv API rate limit exceeded after 3 retries")
    sys.exit(1)
```

#### Error: Network Timeout

**Cause**: Slow network or arXiv server issues

**Handling**:
```python
try:
    response = requests.get(url, timeout=30)
except requests.Timeout:
    print("✗ Error: Request to arXiv API timed out")
    print("  Please check your network connection and try again")
    sys.exit(1)
```

### Semantic Scholar API Errors

#### Error: API Key Invalid

**Cause**: Invalid or expired API key

**Detection**:
```python
if response.status_code == 401:
    # Invalid API key
```

**Handling**:
```python
print("⚠ Warning: Semantic Scholar API key is invalid")
print("  Continuing without citation data")
print("  To fix: Set SEMANTIC_SCHOLAR_API_KEY in .env file")

# Continue without citation data
citations = {
    "cited_by_count": 0,
    "references_count": 0,
    "related_papers": []
}
```

**User Message**:
```
⚠ Warning: Semantic Scholar API key is invalid
  Continuing without citation data
  To fix: Set SEMANTIC_SCHOLAR_API_KEY in .env file
```

#### Error: Paper Not Found in Semantic Scholar

**Cause**: Paper not yet indexed by Semantic Scholar

**Handling**:
```python
if response.status_code == 404:
    print(f"⚠ Warning: Paper {arxiv_id} not found in Semantic Scholar")
    print("  This is normal for very recent papers")
    print("  Continuing without citation data")

    # Continue without citation data
    citations = {
        "cited_by_count": 0,
        "references_count": 0,
        "related_papers": []
    }
```

#### Error: Rate Limit Without API Key

**Cause**: Exceeded free tier limit (100 requests per 5 minutes)

**Handling**:
```python
if response.status_code == 429 and not SEMANTIC_SCHOLAR_API_KEY:
    print("⚠ Warning: Semantic Scholar rate limit exceeded")
    print("  Continuing without citation data")
    print("  To increase limit: Get API key from https://www.semanticscholar.org/product/api")

    # Continue without citation data
    citations = None
```

### Context7 API Errors

#### Error: Library Not Found

**Cause**: Library not available in Context7

**Handling**:
```python
try:
    lib_id = resolve_library_id(library_name, query)
except LibraryNotFoundError:
    print(f"⚠ Warning: Library '{library_name}' not found in Context7")
    print(f"  Continuing with built-in knowledge")

    # Use built-in knowledge instead
    docs = None
```

#### Error: Context7 Unavailable

**Cause**: Context7 MCP server not running or not configured

**Handling**:
```python
if not context7_available:
    print("⚠ Info: Context7 not available")
    print("  Using built-in knowledge for implementation")

    # Proceed without Context7
    docs = None
```

## File System Errors

### Error: Permission Denied

**Cause**: Insufficient permissions to read/write files

**Handling**:
```python
try:
    with open(file_path, 'w') as f:
        f.write(content)
except PermissionError:
    print(f"✗ Error: Permission denied writing to {file_path}")
    print(f"  Please check file permissions and try again")
    sys.exit(1)
```

### Error: Disk Full

**Cause**: Insufficient disk space

**Detection**:
```python
import shutil
usage = shutil.disk_usage(path)
if usage.free < 2 * 1024 * 1024 * 1024:  # Less than 2GB free
    # Disk space low
```

**Handling**:
```python
try:
    # Save file
    with open(file_path, 'wb') as f:
        f.write(data)
except OSError as e:
    if e.errno == 28:  # No space left on device
        print("✗ Error: Insufficient disk space")
        print(f"  Required: ~2GB, Available: {usage.free / 1024**3:.1f}GB")
        print("  Please free up disk space and try again")
        sys.exit(1)
```

### Error: File Not Found

**Cause**: Expected file doesn't exist

**Handling**:
```python
if not os.path.exists(file_path):
    print(f"✗ Error: File not found: {file_path}")
    print(f"  Expected file is missing")

    # Try to recover
    if file_path.endswith(".pdf"):
        print(f"  Attempting to re-download PDF...")
        download_pdf(arxiv_id)
    else:
        sys.exit(1)
```

### Error: Path Too Long (Windows)

**Cause**: Windows path length limit (260 characters)

**Handling**:
```python
if sys.platform == 'win32' and len(file_path) > 260:
    # Use extended-length path syntax
    if not file_path.startswith('\\\\?\\'):
        file_path = '\\\\?\\' + os.path.abspath(file_path)
```

## Execution Errors

### Error: Timeout During Reproduction

**Cause**: Code execution exceeded time limit

**Handling**:
```python
try:
    result = subprocess.run(
        command,
        timeout=TIMEOUT_LIMITS[depth],
        capture_output=True
    )
except subprocess.TimeoutExpired:
    print(f"⚠ Warning: Reproduction timed out after {TIMEOUT_LIMITS[depth]}s")
    print(f"  Marking as partial completion")

    # Log to report
    reproduction_status = "partial"
    reproduction_notes = f"Timed out after {TIMEOUT_LIMITS[depth]}s"

    # Preserve files for debugging
    preserve_sandbox_files()
```

**Report Entry**:
```markdown
## 代码复现状态

- **状态**: 部分成功
- **方法**: 自实现
- **迭代次数**: 3
- **备注**: 执行超时（30分钟限制）。代码已保存至沙箱供调试。建议增加超时限制或优化实现。
```

### Error: Import Error During Reproduction

**Cause**: Missing dependencies

**Handling**:
```python
if "ModuleNotFoundError" in error_message or "ImportError" in error_message:
    # Extract missing module name
    missing_module = extract_module_name(error_message)

    print(f"⚠ Warning: Missing dependency: {missing_module}")
    print(f"  Attempting to install...")

    try:
        subprocess.run(["uv", "pip", "install", missing_module], check=True)
        print(f"✓ Installed {missing_module}")

        # Retry execution
        return retry_execution()
    except subprocess.CalledProcessError:
        print(f"✗ Failed to install {missing_module}")
        print(f"  Continuing to next iteration...")
```

### Error: Syntax Error in Generated Code

**Cause**: Code generation produced invalid Python

**Handling**:
```python
try:
    compile(code, '<string>', 'exec')
except SyntaxError as e:
    print(f"⚠ Warning: Generated code has syntax error at line {e.lineno}")
    print(f"  Error: {e.msg}")

    # Add to error context for next iteration
    errors_from_last_iteration = {
        "type": "SyntaxError",
        "line": e.lineno,
        "message": e.msg,
        "code_snippet": get_code_context(code, e.lineno)
    }

    # Continue to next iteration
    continue
```

### Error: Runtime Error During Reproduction

**Cause**: Code runs but produces errors

**Handling**:
```python
result = subprocess.run(command, capture_output=True, text=True)

if result.returncode != 0:
    print(f"⚠ Warning: Execution failed with exit code {result.returncode}")
    print(f"  Error output:")
    print(f"  {result.stderr[:500]}")  # First 500 chars

    # Analyze error
    error_type = classify_error(result.stderr)

    if error_type == "CUDA_OUT_OF_MEMORY":
        print(f"  Suggestion: Reduce batch size or model size")
    elif error_type == "FILE_NOT_FOUND":
        print(f"  Suggestion: Check data paths and file locations")
    elif error_type == "DIMENSION_MISMATCH":
        print(f"  Suggestion: Verify tensor shapes and dimensions")

    # Add to error context
    errors_from_last_iteration = {
        "type": error_type,
        "stderr": result.stderr,
        "stdout": result.stdout,
        "exit_code": result.returncode
    }
```

## Resource Limit Errors

### Error: Memory Limit Exceeded

**Cause**: Code uses more than 4GB memory

**Detection**:
```python
import psutil

process = psutil.Process()
memory_usage = process.memory_info().rss / 1024**3  # GB

if memory_usage > 4.0:
    # Memory limit exceeded
```

**Handling**:
```python
if "MemoryError" in error_message or "OOM" in error_message:
    print("✗ Error: Memory limit exceeded (4GB)")
    print("  Suggestions:")
    print("  1. Reduce batch size")
    print("  2. Use smaller model variant")
    print("  3. Enable gradient checkpointing")
    print("  4. Use mixed precision training")

    # Mark as failed
    reproduction_status = "failed"
    reproduction_notes = "Memory limit exceeded. Suggest lighter implementation."

    # Preserve files
    preserve_sandbox_files()
```

### Error: Disk Limit Exceeded

**Cause**: Sandbox uses more than 2GB disk space

**Handling**:
```python
sandbox_size = get_directory_size(sandbox_path)

if sandbox_size > 2 * 1024**3:  # 2GB
    print("✗ Error: Sandbox disk limit exceeded (2GB)")
    print(f"  Current usage: {sandbox_size / 1024**3:.1f}GB")
    print("  Cleaning up large files...")

    # Clean up
    cleanup_large_files(sandbox_path)

    # If still over limit
    if get_directory_size(sandbox_path) > 2 * 1024**3:
        print("✗ Unable to reduce disk usage below limit")
        reproduction_status = "failed"
        reproduction_notes = "Disk limit exceeded"
```

### Error: Too Many Open Files

**Cause**: File descriptor limit reached

**Handling**:
```python
try:
    with open(file_path) as f:
        content = f.read()
except OSError as e:
    if e.errno == 24:  # Too many open files
        print("✗ Error: Too many open files")
        print("  Closing unused file handles...")

        # Force garbage collection
        import gc
        gc.collect()

        # Retry
        with open(file_path) as f:
            content = f.read()
```

## Network Errors

### Error: Connection Refused

**Cause**: Server not reachable

**Handling**:
```python
try:
    response = requests.get(url)
except requests.ConnectionError:
    print(f"✗ Error: Connection refused to {url}")
    print("  Please check:")
    print("  1. Network connection")
    print("  2. Firewall settings")
    print("  3. Server availability")
    sys.exit(1)
```

### Error: SSL Certificate Verification Failed

**Cause**: SSL certificate issues

**Handling**:
```python
try:
    response = requests.get(url, verify=True)
except requests.SSLError:
    print("⚠ Warning: SSL certificate verification failed")
    print("  Retrying with verification disabled (not recommended for production)")

    # Retry without verification
    response = requests.get(url, verify=False)
```

### Error: DNS Resolution Failed

**Cause**: Cannot resolve hostname

**Handling**:
```python
try:
    response = requests.get(url)
except requests.exceptions.ConnectionError as e:
    if "Name or service not known" in str(e):
        print(f"✗ Error: Cannot resolve hostname: {url}")
        print("  Please check:")
        print("  1. DNS settings")
        print("  2. Internet connection")
        print("  3. URL spelling")
        sys.exit(1)
```

## Parsing Errors

### Error: PDF Parsing Failed

**Cause**: Corrupted or encrypted PDF

**Handling**:
```python
try:
    pdf_content = read_pdf(pdf_path)
except PDFError as e:
    print(f"✗ Error: Failed to parse PDF: {e}")

    # Try alternative parser
    print("  Trying alternative PDF parser...")
    try:
        pdf_content = read_pdf_alternative(pdf_path)
        print("✓ Successfully parsed with alternative parser")
    except:
        print("✗ All PDF parsers failed")
        print("  Continuing with metadata only")
        pdf_content = None
```

### Error: XML Parsing Failed (arXiv API)

**Cause**: Malformed XML response

**Handling**:
```python
try:
    root = ET.fromstring(response.content)
except ET.ParseError as e:
    print(f"✗ Error: Failed to parse arXiv API response: {e}")
    print(f"  Response content: {response.content[:200]}")

    # Retry with different parser
    try:
        from lxml import etree
        root = etree.fromstring(response.content)
    except:
        print("✗ All XML parsers failed")
        sys.exit(1)
```

### Error: JSON Parsing Failed

**Cause**: Invalid JSON response

**Handling**:
```python
try:
    data = json.loads(response.text)
except json.JSONDecodeError as e:
    print(f"✗ Error: Failed to parse JSON response: {e}")
    print(f"  Response: {response.text[:200]}")

    # Try to extract partial data
    try:
        # Remove trailing garbage
        clean_text = response.text[:response.text.rfind('}') + 1]
        data = json.loads(clean_text)
        print("✓ Recovered partial JSON data")
    except:
        print("✗ Cannot recover JSON data")
        sys.exit(1)
```

## Error Recovery Strategies

### Strategy 1: Exponential Backoff

For transient errors (network, rate limits):

```python
def retry_with_backoff(func, max_retries=3, base_delay=1):
    for attempt in range(max_retries):
        try:
            return func()
        except TransientError as e:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt)
            print(f"Retry {attempt + 1}/{max_retries} after {delay}s...")
            time.sleep(delay)
```

### Strategy 2: Graceful Degradation

Continue with reduced functionality:

```python
try:
    citations = fetch_citations(arxiv_id)
except APIError:
    print("⚠ Warning: Citation data unavailable")
    citations = None  # Continue without citations
```

### Strategy 3: Alternative Approaches

Try different methods:

```python
# Try official repo first
try:
    repo_url = find_official_repo(arxiv_id)
    clone_and_run(repo_url)
except RepoNotFoundError:
    # Fall back to self-implementation
    print("Official repo not found, implementing from scratch...")
    self_implement(arxiv_id)
```

### Strategy 4: Checkpoint and Resume

Save progress for long-running tasks:

```python
checkpoint_file = f"./alpha-sight/.checkpoints/{arxiv_id}.json"

# Save checkpoint
def save_checkpoint(state):
    with open(checkpoint_file, 'w') as f:
        json.dump(state, f)

# Resume from checkpoint
def resume_from_checkpoint():
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file) as f:
            return json.load(f)
    return None
```

## Error Logging

### Log Format

```python
import logging

logging.basicConfig(
    filename=f'./alpha-sight/logs/{arxiv_id}.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log errors
logging.error(f"Failed to fetch paper {arxiv_id}: {error}")
logging.warning(f"Citation data unavailable for {arxiv_id}")
logging.info(f"Successfully analyzed paper {arxiv_id}")
```

### Error Report Section

Include in final report:

```markdown
## 错误和警告

### 警告
- Semantic Scholar API 不可用，未包含引用数据
- 论文较新，部分章节识别可能不准确

### 错误
- 无（分析成功完成）

### 调试信息
- 日志文件: `./alpha-sight/logs/2401.12345.log`
- 沙箱路径: `./alpha-sight/sandbox/2401.12345_reproduction/`
```

## Best Practices

1. **Always validate input** before processing
2. **Use timeouts** for all network requests
3. **Implement retries** with exponential backoff
4. **Log all errors** with context
5. **Provide actionable messages** to users
6. **Clean up resources** in finally blocks
7. **Preserve state** on critical errors
8. **Test error paths** during development
9. **Document error codes** and meanings
10. **Monitor error rates** in production
