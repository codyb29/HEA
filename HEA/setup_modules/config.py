from configparser import ConfigParser


def config(eaObj, path):
    eaObj.cfg = ConfigParser()  # Enables to the easy extraction of configuration files
    # When optionxform(...) is called, it will assign the argument to itself.
    eaObj.cfg.optionxform = lambda option: option
    eaObj.cfg.read(path)  # Extracts the path of the init file.
