# cli.py
import argparse
from todo_app.todo import TodoManager

def main():
    parser = argparse.ArgumentParser(prog="todo", description="Simple Todo CLI")
    parser.add_argument("--file", help="Archivo JSON para guardar todos", default="todos.json")

    sub = parser.add_subparsers(dest="command")

    add_p = sub.add_parser("add", help="Agregar una nueva tarea")
    add_p.add_argument("text", nargs="+", help="Texto de la tarea")

    sub.add_parser("list", help="Listar tareas")

    done_p = sub.add_parser("done", help="Marcar tarea como completada")
    done_p.add_argument("id", help="ID de la tarea")

    del_p = sub.add_parser("delete", help="Borrar una tarea")
    del_p.add_argument("id", help="ID de la tarea")

    args = parser.parse_args()
    manager = TodoManager(storage_file=args.file)

    if args.command == "add":
        text = " ".join(args.text)
        todo = manager.add(text)
        print(f"Agregada: {todo.id} - {todo.text}")
    elif args.command == "list":
        todos = manager.list()
        if not todos:
            print("No hay tareas.")
        for t in todos:
            status = "[x]" if t.done else "[ ]"
            print(f"{t.id} {status} {t.text}")
    elif args.command == "done":
        if manager.complete(args.id):
            print("Tarea marcada como completada.")
        else:
            print("ID no encontrado.")
    elif args.command == "delete":
        if manager.delete(args.id):
            print("Tarea eliminada.")
        else:
            print("ID no encontrado.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
