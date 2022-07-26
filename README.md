# thread-with-results
A python3 threading module with results.

You can easily get the thread's response result and return value like this

```python
task = ThreadWithResult(
    func,
    *args,
    **kwds
)
task.start()
task.join()

# now you can get the results
print(task.done, task.timeout, task.error, task.results)
```
