package com.ecommerce.user.service;

import com.ecommerce.user.entity.User;
import com.ecommerce.user.repository.UserRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private UserService userService;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void testCreateUser_Success() {
        User user = new User("Mugdho", "mugdho@test.com");
        when(userRepository.existsByEmail("mugdho@test.com")).thenReturn(false);
        when(userRepository.save(user)).thenReturn(user);

        User created = userService.createUser(user);
        assertNotNull(created);
        assertEquals("Mugdho", created.getName());
    }

    @Test
    void testCreateUser_DuplicateEmail() {
        User user = new User("Mugdho", "mugdho@test.com");
        when(userRepository.existsByEmail("mugdho@test.com")).thenReturn(true);

        assertThrows(RuntimeException.class, () -> userService.createUser(user));
    }

    @Test
    void testGetUserById_Found() {
        User user = new User("Mugdho", "mugdho@test.com");
        user.setId(1L);
        when(userRepository.findById(1L)).thenReturn(Optional.of(user));

        Optional<User> found = userService.getUserById(1L);
        assertTrue(found.isPresent());
        assertEquals("Mugdho", found.get().getName());
    }

    @Test
    void testGetUserById_NotFound() {
        when(userRepository.findById(99L)).thenReturn(Optional.empty());
        Optional<User> found = userService.getUserById(99L);
        assertFalse(found.isPresent());
    }
}
