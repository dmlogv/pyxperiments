"""Commit a bunch of forgotten files"""

import ast
import datetime
import operator
import os
import os.path
import subprocess


class FileInfo:
    """File information"""
    def __init__(self, path: str, created_at: datetime.datetime, doc: str):
        self.path = path
        self.created_at = created_at
        self.doc = doc
    
    def __repr__(self):
        return f'<{self.__class__.__name__} {self.path:>25} "{self.created_at}": "{self.doc}"'


def get_file_doc(path):
    """Load __doc__ from `.py` file"""
    with open(path) as f:
        module = ast.parse(f.read())
        return ast.get_docstring(module)


def get_files(path='.'):
    """Load `.py` files information"""
    files = []
    
    for f in os.listdir(path):
        if f.endswith('.py'):
            created_at = datetime.datetime.fromtimestamp(os.path.getctime(f))
            doc: str = get_file_doc(f)
            doc_header = doc.splitlines()[0] if doc else doc
        
            files.append(FileInfo(f, created_at, doc_header))
    
    return files


def commit_file(f: FileInfo):
    print(f)

    dtm = f.created_at.isoformat()

    md = f'- [`{f.path}`](/{f.path}) — {f.doc}\n'
    add = ['git', 'add', f'{f.path}']
    commit = ['git', 'commit', '-am', f'Add {f.path}', '--date', f'{dtm}']

    print(md)
    with open('README.md', 'a', encoding='utf-8') as rm:
        rm.write(md)
    
    print(add)
    print(subprocess.run(add, capture_output=True))
    
    print(commit)
    print(subprocess.run(commit, env={'GIT_COMMITTER_DATE': dtm}, capture_output=True))
    
    print()


if __name__ == '__main__':
    for f in sorted(get_files(), key=operator.attrgetter('created_at')):
        commit_file(f)