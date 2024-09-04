package geohanz.practice.registration_login_demo.service;

import geohanz.practice.registration_login_demo.dto.UserDto;
import geohanz.practice.registration_login_demo.entity.User;

import java.util.List;

public interface UserService {

    void saveUser(UserDto userDto);

    User findUserByEmail(String email);

    List<UserDto> findAllUsers();

}
