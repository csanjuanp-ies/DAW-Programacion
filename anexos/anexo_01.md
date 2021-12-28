# Anexo 1
## Cambios en las nuevas versiones
### 3.10
#### Patrón estructural

Hasta ahora no existían una estructura sintáctica que reflejara el caso según (switch) de otros lenguajes, 
debíamos usar estructuras if-else andadas. A partir de esta versión aparece este patrón que aumenta las capacidades 
de la sentencia switch (según) dando unas capacidades extendidas.

**Caso implementado en otros lenguajes**
```
match thing:

        case 1:
            print("thing is 1")
        case 2:
            print("thing is 2")
        case 3:
            print("thing is 3")
        case _:
            print("thing is not 1, 2 or 3")

match args.command
    case 'push':
        print('pushing')
    case 'pull':
        print('pulling')
    case _:
        parser.error(f'{args.command!r} not yet implemented')
```
**Caso con listas:**
```
for thing in [[1,2],[9,10],[1,2,3],[1],[0,0,0,0,0]]:
    match thing:
        case [x]:
            print(f"single value: {x}")
        case [x,y]:
            print(f"two values: {x} and {y}")
        case [x,y,z]:
            print(f"three values: {x}, {y} and {z}")       
        case _:
            print("too many values")

for thing in [[1,2],[9,10],[3,4],[1,2,3],[1],[0,0,0,0,0]]:
    match thing:
        case [x]:
            print(f"single value: {x}")
        case [1,y]:
            print(f"two values: 1 and {y}")
        case [x,10]:
            print(f"two values: {x} and 10")
        case [x,y]:
            print(f"two values: {x} and {y}")
        case [x,y,z]:
            print(f"three values: {x}, {y} and {z}")       
        case _:
            print("too many values")

for thing in [[1,2,3,4],['a','b','c'],"this won't be matched"]:
    match thing:
        case [*y]:
            for i in y:
                print(i)
        case _:
            print("unknown")


match event.get()
    case Click((x, y), button=Button.LEFT):  
        handle_click_at(x, y)
    case Click():
        pass  # ignore other clicks
    case KeyPress(key_name="Q") | Quit():
        game.quit()
    case KeyPress(key_name="up arrow"):
        game.go_north()
    ...
    case KeyPress():
        pass # Ignore other keystrokes
    case other_event:
        raise ValueError(f"Unrecognized event: {other_event}")

match expr
        case BinaryOp('+', left, right):
            return eval_expr(left) + eval_expr(right)
        case BinaryOp('-', left, right):
            return eval_expr(left) - eval_expr(right)
        case BinaryOp('*', left, right):
            return eval_expr(left) * eval_expr(right)
        case BinaryOp('/', left, right):
            return eval_expr(left) / eval_expr(right)
        case UnaryOp('+', arg):
            return eval_expr(arg)
        case UnaryOp('-', arg):
            return -eval_expr(arg)
        case VarExpr(name):
            raise ValueError(f"Unknown value of: {name}")
        case float() | int():
            return expr
        case _:
            raise ValueError(f"Invalid expression value:{repr(expr)}")
```