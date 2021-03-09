import os
import warnings
import subprocess

warnings.simplefilter("ignore", ResourceWarning)


# brew install zenity

################################################################################
def zen_func(op, parameter=None, value=None):
    try:
        if len(parameter) != len(value):
            raise IOError(
                'The lengths of the lists of parameters and values are '
                'different.')
        cmd = ['zenity', f'--{op}']
        if len(parameter) > 0:
            for i in range(len(parameter)):
                cmd.append('--' + str(parameter[i]) + '=' + str(value[i]))
        po = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=None)
        t = po.communicate()[0].decode("utf-8")
        print(t.rstrip('\r\n'), end='')
        return 0
    except Exception as err:
        msg = str(err)
        print('%s%s' % (msg, os.linesep))
        return 1


################################################################################
zen_func('calendar', ['date-format', 'day', 'month', 'year',
                      'text', 'width', 'height', 'timeout',
                      'ok-label', 'cancel-label'],
         ['%Y-%m-%d', '12', '10', '2022',
          'Test Zenity Calendar', '200', '200', '5',
          'OK', 'Exit'])
