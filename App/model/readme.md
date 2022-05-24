### Document for Database.
___
**Example**

1. getDate

output:
```
['20220524', '20220523']
year: 2022, month: 05, day: 24
year: 2022, month: 05, day: 23

```

2. getHistoryOnDate

output
```
[
    {
        'id': 1, 
        'type': 'test',
        'value': 100, 
        'datetime': '192926'
    }, 
    {
        'id': 2, 
        'type': 'test', 
        'value': 100, 
        'datetime': '192929'
    }, 
    {
        'id': 3, 
        'type': 'test', 
        'value': 100, 
        'datetime': '193430'
    }
]
```
use convert json to more intuitive or json library

3. getHistoryAllDate

output
```
{
    "20220524": [
        {
            'id': 1, 
            'type': 'test',
            'value': 100, 
            'datetime': '192926'
        }, 
        {
            'id': 2, 
            'type': 'test', 
            'value': 100, 
            'datetime': '192929'
        }, 
        {
            'id': 3, 
            'type': 'test', 
            'value': 100, 
            'datetime': '193430'
        }
    ]

    "20220523":[

    ]
}
```
use convert json to more intuitive or json library

See All on [Document][./database.html]
