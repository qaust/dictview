"""
Finds path thru dict to desired key
"""

from    collections import deque, namedtuple

DictPath = namedtuple("DictPath", ["value", "path"])

def seek(d: dict, tgt: list|tuple, strategy="dfs"):

    paths = []

    def seek_dfs(d, tgt, idx=0, current_path=None):
        
        # Base case: current path is not given
        if current_path is None:
            current_path = []

        # Base case: sequence has been fully matched
        if idx == len(tgt):
            return current_path
        
        for k, v in d.items():
            new_path = current_path + [k]
            candidate = DictPath(value=v, path=new_path)
            # If key matches current part of sequence, look deeper 
            if k == tgt[idx]:
                # If it is the last key in the sequence, it's a match
                if idx == len(tgt) - 1 and candidate not in paths:
                    paths.append(candidate)
                # Otherwise continue deeper into the sequence
                if isinstance(v, dict):
                    result = seek_dfs(v, tgt, idx=idx + 1, current_path=new_path)
                    if result is not None and candidate not in paths:
                        paths.append(candidate)
            # If not, look deeper into the dict, but not the sequence
            if isinstance(v, dict):
                result = seek_dfs(v, tgt, idx=idx, current_path=new_path)
                if result is not None and candidate not in paths:
                    paths.append(candidate)

    def seek_bfs(d, tgt, current_path=None):
        raise NotImplementedError


    def seek_hybrid(d, tgt, current_path=None):
        raise NotImplementedError

    if strategy=="dfs":
        seek_dfs(d, tgt)
    elif strategy=="bfs":
        seek_bfs(d, tgt)
    elif strategy=="hybrid":
        seek_hybrid(d, tgt)
    else:
        raise ValueError("Strategy should be one of ['dfs', 'bfs', 'hybrid']")

    try:
        assert len(paths) == 1, f"Expected 1 path, got {len(paths)}."
        return paths[0]
    except AssertionError as e:
        if len(paths) > 1:
            print("Try a more specific (longer) target")
        elif len(paths) == 1:
            print("Target not found.")
        else:
            print(e)
        return DictPath(value=None, path=None)

    