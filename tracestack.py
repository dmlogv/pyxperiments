"""Just used `tracestack` to find an error explanation. Need `tracestack`"""

from tracestack import trace


@trace
def exc():
    return 1/0

exc()
