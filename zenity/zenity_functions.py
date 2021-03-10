import os
import warnings
import subprocess

warnings.simplefilter("ignore", ResourceWarning)


# brew install zenity
# zenity --help

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
                if parameter[i] and value[i]:
                    cmd.append('--' + str(parameter[i]) + '=' + str(value[i]))
                else:
                    cmd.append(parameter[i])
        po = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=None)
        t = po.communicate()[0].decode("utf-8")
        print(t.rstrip('\r\n'), end='')
        return 0
    except Exception as err:
        msg = str(err)
        print('%s%s' % (msg, os.linesep))
        return 1


################################################################################
# OP Type 1: Calendar
# Available Parameters:
'''
date-format, day, month, year, text, width, height, timeout, ok-label, cancel-label
'''
op = 'calendar'
params = ['date-format', 'day', 'month', 'year',
          'text', 'width', 'height', 'timeout',
          'ok-label', 'cancel-label']
val = ['%Y-%m-%d', '12', '10', '2022',
       'Test Zenity Calendar', '200', '200', '5',
       'OK', 'Exit']
# return value: 2022-10-12

# ==============================================================================
'''
OP Type 2: Color - Display color selection dialog
Available Parameters: color, palette, timeout
'''
op = 'color-selection'
params = ['color', 'show-palette', 'timeout']
val = ['pink', '', '5']
# return value: rgb(255,192,203)

# ==============================================================================
'''
OP Type 3: Error - Display error dialog
Available Parameters: no wrap, no markup, ellipsize, text, icon-name, width, height, timeout, ok-label
'''
op = 'error'
params = ['no-wrap', 'no-markup', 'ellipsize', 'text', 'icon-name', 'width', 'height', 'timeout', 'ok-label']
val = ['', '', '', 'Unknown file is detected', 'dialog-warning', '200', '200', '5', 'Proceed']

# ==============================================================================
'''
OP Type 4: Info - Display info dialog
Available Parameters: no wrap, no markup, text, icon, width, height, timeout, ok-label
'''
op = 'info'
params = ['no-wrap', 'no-markup', 'text', 'icon-name', 'width', 'height', 'timeout', 'ok-label']
val = ['', '', 'Information', 'dialog-information', '200', '200', '5', 'Proceed']
zen_func(op, params, val)

# ...