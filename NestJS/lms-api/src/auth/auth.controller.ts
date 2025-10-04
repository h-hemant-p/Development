import { Body, Controller, Get, Post } from '@nestjs/common';
import { AuthService } from './auth.service';
import { RegisterUserDto } from './dto/registerUser.dto';

@Controller('auth')
export class AuthController {
    constructor(private readonly authService: AuthService) {}
    
    @Post('register')
    registerUser(@Body() registerUserDto: RegisterUserDto){
        const result = this.authService.registerUser(registerUserDto);
        return result;
    }
}
