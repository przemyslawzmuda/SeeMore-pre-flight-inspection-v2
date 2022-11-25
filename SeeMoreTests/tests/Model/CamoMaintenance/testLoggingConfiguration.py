from tempfile import TemporaryDirectory

from SeeMore.Model.CamoMaintenance.LoggingConfiguration import *


def test_return_name_for_logger_object():
    with TemporaryDirectory() as temporary_dir:
        # given
        temporary_dir = Path(temporary_dir)
        mock_project_dir = temporary_dir / 'user-x/Python-Project/SeeMore/App/main-test.py'
        # when
        name_for_logger_object = SeeMoreLoggingFacility.return_name_for_logger_object(mock_project_dir)
        # then
        assert name_for_logger_object == 'SeeMore/App/main-test.py'
