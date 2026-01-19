# todo_app/todo.py
from dataclasses import dataclass, asdict
from typing import List, Optional
from uuid import uuid4
from .storage import load_json, save_json

DEFAULT_FILE = "todos.json"

@dataclass
class Todo:
    id: str
    text: str
    done: bool = False

    @staticmethod
    def create(text: str) -> "Todo":
        return Todo(
            id=str(uuid4()), 
            text=text, 
            done=False
            )

class TodoManager:
    def __init__(self, storage_file: str = DEFAULT_FILE):
        self.storage_file = storage_file
        self.todos: List[Todo] = self._load()

    def _load(self) -> List[Todo]:
        raw = load_json(self.storage_file)
        return [Todo(**item) for item in raw]

    def _save(self) -> None:
        save_json(self.storage_file, [asdict(t) for t in self.todos])

    def add(self, text: str) -> Todo:
        todo = Todo.create(text)
        self.todos.append(todo)
        self._save()
        return todo

    def list(self) -> List[Todo]:
        return self.todos

    def find(self, todo_id: str) -> Optional[Todo]:
        for t in self.todos:
            if t.id == todo_id:
                return t
        return None

    def complete(self, todo_id: str) -> bool:
        t = self.find(todo_id)
        if not t:
            return False
        t.done = True
        self._save()
        return True

    def delete(self, todo_id: str) -> bool:
        before = len(self.todos)
        self.todos = [t for t in self.todos if t.id != todo_id]
        changed = len(self.todos) != before
        if changed:
            self._save()
        return changed
