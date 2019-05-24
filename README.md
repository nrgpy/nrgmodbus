# <img alt="NRGPy" src="https://www.nrgsystems.com/mysite/images/logo.png?v=3" height="40">

'''nrgmodbus''' is a Python package for making modbus connections to NRG devices.


## Installation:

```python
# from the directory containing this README file:
pip install -e .
```

## Examples:

### Single polling:

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

### Automatic polling:

```python
In [1]: from nrgmodbus.nrgmodbus import ipackaccess

In [2]: poller = ipackaccess(ip='192.168.178.168', connect=True)
Connecting to 192.168.178.168...                [OK]

In [3]: poller.poll(interval=4, echo=True)

1       2019-5-24 1:23:7        0.2101999968290329      0.05000000074505806
2       2019-5-24 1:23:11       0.2101999968290329      0.05000000074505806
3       2019-5-24 1:23:15       0.2101999968290329      0.05000000074505806

...

37      2019-5-24 1:25:31       0.2101999968290329      0.05000000074505806
38      2019-5-24 1:25:35       0.2101999968290329      0.05000000074505806
39      2019-5-24 1:25:39       0.2101999968290329      0.05000000074505806
40      2019-5-24 1:25:43       0.2101999968290329      0.03999999910593033
41      2019-5-24 1:25:47       0.2101999968290329      0.03999999910593033
42      2019-5-24 1:25:51       0.2101999968290329      0.05000000074505806
```
