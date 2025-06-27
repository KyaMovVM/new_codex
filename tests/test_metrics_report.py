import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from metrics_report import analyze_file, collect_metrics


def test_analyze_file(tmp_path):
    sample = tmp_path / 'sample.py'
    sample.write_text(
        """\n
def foo():
    pass

class Bar:
    x = 1
    def method(self):
        pass
"""
    )
    result = analyze_file(str(sample))
    assert result['functions'] == 1
    assert result['classes'] == 1
    assert result['methods'] == 1
    assert result['variables'] == 1
    assert result['lines'] > 0


def test_collect_metrics(tmp_path):
    file1 = tmp_path / 'a.py'
    file1.write_text('def f():\n    pass\n')
    data = collect_metrics(str(tmp_path))
    assert str(file1) in data
