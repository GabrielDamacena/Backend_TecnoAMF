from rest_framework import generics
from .models import Usuario, Semestre
from .serializers import UsuarioSerializer, SemestreSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario

# View para listar e criar usuários
class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# View para detalhar um usuário específico
class UsuarioDetailView(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# View para listar e criar semestres
class SemestreListCreateView(generics.ListCreateAPIView):
    queryset = Semestre.objects.all()
    serializer_class = SemestreSerializer

# View para detalhar um semestre específico
class SemestreDetailView(generics.RetrieveAPIView):
    queryset = Semestre.objects.all()
    serializer_class = SemestreSerializer

class SemestrePorUsuarioListView(generics.ListAPIView):
    serializer_class = SemestreSerializer

    def get_queryset(self):
        usuario_id = self.kwargs['usuario_id']
        return Semestre.objects.filter(usuario_id=usuario_id)
    
class LoginView(APIView):
    def post(self, request):
        usuario_id = request.data.get('id')
        cpf = request.data.get('cpf')

        try:
            # Verifica se o usuário existe
            usuario = Usuario.objects.get(id=usuario_id)
            if usuario.cpf == cpf:
                return Response({
                    "message": "Login realizado com sucesso!",
                    "usuario_id": usuario.id,
                    "matricula": usuario.matricula
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "message": "CPF incorreto."
                }, status=status.HTTP_401_UNAUTHORIZED)
        except Usuario.DoesNotExist:
            return Response({
                "message": "Usuário não encontrado."
            }, status=status.HTTP_404_NOT_FOUND)