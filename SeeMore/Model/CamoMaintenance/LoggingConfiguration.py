from pathlib import Path


class SeeMoreLoggingFacility:
    """The SeeMoreLoggingFacility gives everything what is necessary to report and record progress as well as
    problems, moreover the destiny is to help developer track down bugs and leave a record how the code is being used.
    The ultimate goal of that class is to improve reliable of the code.
    Available levels for loggers object: NOTSET: 0, DEBUG: 10, INFO: 20, WARNING: 30, ERROR: 40, CRITICAL: 50.
    """

    @staticmethod
    def return_name_for_logger_object(file_name: str) -> str:
        """The following function returns the name for a logger object in a given script.
        Args:
            file_name (str): A root path to the following script.
                For instance: /Home/User/ProjectDirectory/SeeMore/App/ScriptName.py
        Returns:
             str: Name for a logger object for a given script.
        """
        # type(__file__) = <class 'str'>
        file_name_parts_list = Path(file_name).parts

        # In order to hide the Home directory of the user, perform the following logic:
        index_for_project_name = file_name_parts_list.index('SeeMore')
        start_index_for_logger_name = len(file_name_parts_list) - index_for_project_name
        name_for_logger_object = '/'.join(file_name_parts_list[-start_index_for_logger_name:])
        return name_for_logger_object
