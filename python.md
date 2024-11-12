# multiprocessing

|Method|Blocking|Multiple Input Arguments|Result Type|Return Type|Input Order Maintained|
|-|-|-|-|-|-|
|apply|Yes|No|Single result|Result (object)|Yes|
|apply_async|No|No|Single result|AsyncResult|No|
|map|Yes|No|Iterable|List|Yes|
|map_async|No|No|Iterable|AsyncResult|No|
|imap|No|No|Iterable|Iterator|Yes|
|imap_unordered|No|No|Iterable|Iterator|No|
|starmap|Yes|Yes|Iterable|List|Yes|
|starmap_async|No|Yes|Iterable|AsyncResult|No|
