# TODO

| format 1 | dots | format 2 | dots | works | example             |
| -------- | ---- | -------- | ---- | ----- | ------------------- |
| AM       | ✔️   | AM       | ✔️   |       | 9:30 AM to 10:40 AM |
| AM       | ❎   | AM       | ✔️   |       | 9 AM to 10:40 AM    |
| AM       | ✔️   | AM       | ❎   |       | 9:30 AM to 10 AM    |
| AM       | ❎   | AM       | ❎   |       | 9 AM to 10 AM       |
| AM       | ✔️   | PM       | ✔️   |       | 9:30 AM to 10:40 PM |
| AM       | ❎   | PM       | ✔️   |       | 9 AM to 10:40 PM    |
| AM       | ✔️   | PM       | ❎   |       | 9:30 AM to 10 PM    |
| AM       | ❎   | PM       | ❎   |       | 9 AM to 10 PM       |
| PM       | ✔️   | PM       | ✔️   |       | 10:40 PM to 9:30 PM |
| PM       | ❎   | PM       | ✔️   |       | 10 PM to 9:30 PM    |
| PM       | ✔️   | PM       | ❎   |       | 10:40 PM to 9 PM    |
| PM       | ❎   | PM       | ❎   |       | 10 PM to 9 PM       |
| PM       | ✔️   | AM       | ✔️   |       | 10:40 PM to 9:30 AM |
| PM       | ❎   | AM       | ✔️   |       | 10 PM to 9:30 AM    |
| PM       | ✔️   | AM       | ❎   |       | 10:40 PM to 9 AM    |
| PM       | ❎   | AM       | ❎   |       | 10 PM to 9 AM       |

leyend:

- ✔️
- ❎
