package geohanz.practice.registration_login_demo.repo;

import geohanz.practice.registration_login_demo.entity.Role;
import org.springframework.data.jpa.repository.JpaRepository;

public interface RoleRepository extends JpaRepository<Role, Long> {

    Role findByName(String name);

}

