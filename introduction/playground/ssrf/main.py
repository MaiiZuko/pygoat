import os


def ssrf_lab(file):
    try:
        dirname = os.path.realpath(os.path.dirname(__file__))
        # Validate and safely construct the file path within the base directory
        if os.path.isabs(file):
            raise ValueError("Invalid file path")
        safe_path = os.path.realpath(os.path.join(dirname, file))
        if os.path.commonpath([dirname, safe_path]) != dirname:
            raise ValueError("Invalid file path")
        filename = safe_path
        file = open(filename,"r")
        data = file.read()
        return {"blog":data}
    except:
        return {"blog": "No blog found"}