from unittest.mock import patch

from src import create_app
from src.services.users_service import UsersService


@patch("src.services.users_service.UsersRepository.get_all")
def test_get_user(get_all):
    app = create_app()
    with app.app_context():
        get_all.return_value = []
        response = UsersService.get_users()
        assert response.status_code == 200
        assert response.json == []
