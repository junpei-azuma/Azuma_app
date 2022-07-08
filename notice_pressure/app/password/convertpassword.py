from werkzeug.security import generate_password_hash
from app.password.passworddto import PasswordDto

class ConvertPassword():
    
    @staticmethod
    def hash(passworddto: PasswordDto) -> PasswordDto:   
        """パスワードをハッシュ化

        Args:
            passworddto (PasswordDto): DTO

        Returns:
            PasswordDto: DTO
        """           
        hashed_password_value: str = generate_password_hash(passworddto.value)
        hashed_passworddto: PasswordDto = PasswordDto(user_id = passworddto.user_id, value = hashed_password_value)
        return hashed_passworddto