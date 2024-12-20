from django.urls import path
from .views import UsuarioListCreateView, UsuarioDetailView, SemestreListCreateView, SemestreDetailView, SemestrePorUsuarioListView, LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('usuarios/', UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),
    path('semestres/', SemestreListCreateView.as_view(), name='semestre-list-create'),
    path('semestres/<int:pk>/', SemestreDetailView.as_view(), name='semestre-detail'),
    path('usuarios/<int:usuario_id>/semestres/', SemestrePorUsuarioListView.as_view(), name='semestre-por-usuario'),
    path('login/', LoginView.as_view(), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
