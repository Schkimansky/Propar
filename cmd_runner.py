import subprocess as sub

def run_command(cmd: str, timeout=None, get_both_output_and_errors=False, get_return_code=False):
    result = sub.run(cmd.split(" "), timeout=timeout)

    if get_both_output_and_errors:
        if get_return_code:
            return result.stdout, result.stderr, result.returncode
        else:
            return result.stdout, result.stderr
    else:
        if get_return_code:
            if result.returncode == 0:
                return result.stdout, result.returncode
            else:
                return result.stderr, result.returncode
        else:
            if result.returncode == 0:
                return result.stdout
            else:
                return result.stderr

# Run multiple commands
def run_commands(cmds: list[str], timeout=None, get_both_output_and_errors=False, get_return_code=False):
    results = []
    for cmd in cmds:
        result = run_command(cmd, timeout, get_both_output_and_errors, get_return_code)
        results.append(result)
    return results
