from rest_framework.viewsets import ModelViewSet

from apps.todo.models import Task
from .serializers import TaskSerializer

class TaskViewSet(ModelViewSet):
    # quero todos os dados que estão na tabela task
    queryset = Task.objects.all() # chamada p banco de dados

    serializer_class = TaskSerializer
