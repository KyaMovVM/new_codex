import ast
import os
import argparse
from typing import Dict, Any


def analyze_file(path: str) -> Dict[str, int]:
    with open(path, 'r', encoding='utf8') as f:
        source = f.read()
    tree = ast.parse(source, filename=path)
    functions = 0
    classes = 0
    methods = 0
    variables = 0
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions += 1
        elif isinstance(node, ast.ClassDef):
            classes += 1
            for subnode in node.body:
                if isinstance(subnode, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    methods += 1
                elif isinstance(subnode, ast.Assign):
                    variables += len(subnode.targets)
        elif isinstance(node, ast.Assign):
            variables += len(node.targets)
    lines = len([line for line in source.splitlines() if line.strip()])
    return {
        'functions': functions,
        'classes': classes,
        'methods': methods,
        'variables': variables,
        'lines': lines,
    }


def collect_metrics(root: str) -> Dict[str, Dict[str, int]]:
    metrics: Dict[str, Dict[str, int]] = {}
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if fname.endswith('.py') and fname != os.path.basename(__file__):
                file_path = os.path.join(dirpath, fname)
                metrics[file_path] = analyze_file(file_path)
    return metrics


def main() -> None:
    parser = argparse.ArgumentParser(description='Генератор отчёта о метриках')
    parser.add_argument('path', nargs='?', default='.', help='Корневая папка проекта')
    parser.add_argument('-o', '--output', help='Файл, в который сохранить отчёт')
    args = parser.parse_args()

    data = collect_metrics(args.path)
    lines = []
    for file, metrics in sorted(data.items()):
        lines.append(f'{file}:')
        for key, value in metrics.items():
            lines.append(f'  {key}: {value}')
    report = '\n'.join(lines)

    if args.output:
        with open(args.output, 'w', encoding='utf8') as f:
            f.write(report)
    else:
        print(report)


if __name__ == '__main__':
    main()
