package geohanz.practice.registration_login_demo.repo;

import geohanz.practice.registration_login_demo.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {

    User findByEmail(String email);

}
