# Vision

What I wish to accomplish is a plugin that easily can provide reports of what function and line something crashes in.

I see this plugin going throug several steps to make this happen:
1) A tree model with every node represented by function and line where it broke

    ```bash
   error_fn:4
   |- calling_fn_a:2
   error_fn:2
   |- calling_fn_b:5
   ```
   Here `error_fn` is the place where it breaks on line 4 and 2 respectively.

2) Extend (1) with grouping by function first and line second:

    ```bash
   error_fn
   |-[3]-calling_fn_b:5
   |-[5]-calling_fn_a:2
   ```
3) Extend (2) with info about what the function was called with

   ```bash
   error_fn
   |-[3](bool)-calling_fn_b:5
   |-[5](bool)-calling_fn_a:2
   ```
    This should be one of the possible views in the final version. Possibly in another format but viewing what types are sent into a function should be possible.
4) An extension to (3) with the actual argument should be implemented aswell but should not be a replacement. Perhaps a `-vv` option

   ```bash
   error_fn
   |-[3](fail_early=False)-calling_fn_b:5
   |-[5](fail_early=True)-calling_fn_a:2
   ```

Perhaps it should be visualized in some other way:

```bash
error_fn failed in 2 places
======= error_fn(fail_early=True) =========
2     if fail_early:
3         raise RuntimeError
4     else:
--------- calling_fn_b -----------
4 def calling_fn_b():
5     error_fn()
6

======= error_fn(fail_early=False) =========
4     else:
5         raise RuntimeError
6
--------- calling_fn_a -----------
1 def calling_fn_a():
2     error_fn(fail_early=False)
3
```

Some time should be committed to making this output as easy to grasp as possible.
