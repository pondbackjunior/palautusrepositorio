class Project:
    def __init__(self, name, description, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return "\n- ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description or '-'}\n"
            f"Dependencies: {self._stringify_dependencies(self.dependencies)}\n"
            f"Development dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
