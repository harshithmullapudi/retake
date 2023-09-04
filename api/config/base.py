import os


class Config:
    def get_property(self, property_name: str) -> str:
        if value := os.environ.get(property_name):
            return value
        else:
            raise EnvironmentError(
                f"{property_name} environment variable is not defined."
            )
