# ![NRGPy](https://www.gravatar.com/avatar/6282094b092c756acc9f7552b164edfe?s=24) nrgmodbus

**nrgmodbus** is a Python package for making modbus connections to NRG devices.

## Requirements

### SymphoniePRO/iPackACCESS

- Logger FW version 3.2.3 / iPackACCESS FW version 2.2.0 (or higher)

## Installation

```python
pip install nrgmodbus
```

## Examples

### iPackACCESS

```python
In [1]: from nrgmodbus.ipackaccess import ipackaccess

In [2]: poller = ipackaccess(ip='192.168.178.168')

In [3]: poller.connect()
Connecting to 192.168.178.168...                [OK]

In [4]: poller.return_diag_readings()

In [5]: poller.hr.diag['12v_bat']['value']
Out[5]: 14.09000015258789

In [6]: poller.hr.diag['temp']['value']
Out[6]: 22.739999771118164

In [7]: poller.return_channel_data(1)

In [8]: poller.hr.data_ch[1]
Out[8]: {'avg': {'reg': [2506, 2], 'value': 6.4},
         'sd': {'reg': [2508, 2], 'value': 2.1},
         'max': {'reg': [2510, 2], 'value': 9.1},
         'min': {'reg': [2512, 2], 'value': 4.6},
         'gust': {'reg': [2514, 2], 'value': 9.0},
         'samp': {'reg': [1506, 2], 'value': 6.2}}
```

## spidar

```python
In [1]: from nrgmodbus.spidar import spidar_v1

In [2]: poller = spidar_v1(ip="192.168.1.1", connect=True)
Connecting to 192.168.1.1...                [OK]

In [3]: poller.return_rt_data_readings()

In [4]: poller.hr.met_data
Out[4]: ...

In [5]: poller.hr.data_ch
Out[5]: ...

```
