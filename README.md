# <img alt="NRGPy" src="https://www.nrgsystems.com/mysite/images/logo.png?v=3" height="40">

'''nrgmodbus''' is a Python package for making modbus connections to NRG devices.


## Installation:

```python
# from the directory containing this README file:
pip install -e .
```

## Example:

```python
In [1]: from nrgmodbus.nrgmodbus import ipackaccess

In [2]: poller = ipackaccess(ip='192.168.178.168')

In [3]: poller.connect()
Connecting to 192.168.178.168...                [OK]

In [4]: poller.return_diag_readings()

In [5]: poller.diag_12v_bat
Out[5]: 14.09000015258789

In [6]: poller.diag_temp
Out[6]: 22.739999771118164

In [7]: poller.return_rt_data_readings()

In [8]: poller.rt_ch1
Out[8]: 0.2101999968290329
```
