import { Injectable } from '@nestjs/common'
import bcrypt from 'bcrypt'
import { UserService } from 'src/user/user.service'
import { RegisterUserDto } from './dto/registerUser.dto'

@Injectable()
export class AuthService {
    constructor(private readonly userService: UserService) { }

    async registerUser(registerUserDto: RegisterUserDto) {

        // Logic for register user
        /**
         * 1. check if email already exists
         * 2. hash the password
         * 3. store the user into db
         * 4. generate jwt token
         * 5. send token in response
         * */
        const saltRounds = 10
        const hash = await bcrypt.hash(registerUserDto.password, saltRounds)
        const user = await this.userService.createUser({ ...registerUserDto, password: hash })
        return {}
    }
}
