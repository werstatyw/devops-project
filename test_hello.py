from click.testing import CliRunner
from hello import calculate


#search(path, ftype):
    
def test_calculate():
  runner = CliRunner()
  result = runner.invoke(calculate, ['--value1', '1', '--value2', '2'])
  assert result.exit_code == 0
  assert '3' in result.output