import { defineStore } from 'pinia'
import axios from 'axios'

// Define and export a store named 'useUserStore'
export const useUserStore = defineStore({
    // Unique identifier for the store
    id: 'user',

    // Define the state of the store
    state: () => ({
        // Initial user state
        user: {
            isAuthenticated: false,
            id: null,
            name: null,
            email: null,
            access: null,
            refresh: null,
            avatar: null
        }
    }),

    // Define actions (methods) that can be performed on the store
    actions: {
        // Action to initialize the user store with data from localStorage
        initStore() {
            // Log the initialization process
            console.log('initStore', localStorage.getItem('user.access'))

            // Check if user has access token in localStorage
            if (localStorage.getItem('user.access')) {
                // Log that user has access
                console.log('User has access!')

                // Initialize user data from localStorage
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.id = localStorage.getItem('user.id')
                this.user.name = localStorage.getItem('user.name')
                this.user.email = localStorage.getItem('user.email')
                this.user.avatar = localStorage.getItem('user.avatar')
                this.user.isAuthenticated = true

                // Refresh access token
                this.refreshToken()

                // Log initialized user data
                console.log('Initialized user:', this.user)
            }
        },

        // Action to set access and refresh tokens
        setToken(data) {
            // Log setting token
            console.log('setToken', data)

            // Set user data from response
            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            // Store tokens in localStorage
            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)

            // Log access token
            console.log('user.access: ', localStorage.getItem('user.access'))
        },

        // Action to remove access and refresh tokens
        removeToken() {
            // Log removing token
            console.log('removeToken')

            // Clear user data
            this.user.refresh = null
            this.user.access = null
            this.user.isAuthenticated = false
            this.user.id = null
            this.user.name = null
            this.user.email = null
            this.user.avatar = null

            // Clear localStorage data
            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.name', '')
            localStorage.setItem('user.email', '')
            localStorage.setItem('user.avatar', '')
        },

        // Action to set user information
        setUserInfo(user) {
            // Log setting user info
            console.log('setUserInfo', user)

            // Set user data
            this.user.id = user.id
            this.user.name = user.name
            this.user.email = user.email
            this.user.avatar = user.avatar

            // Store user data in localStorage
            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.name', this.user.name)
            localStorage.setItem('user.email', this.user.email)
            localStorage.setItem('user.avatar', this.user.avatar)

            // Log user data
            console.log('User', this.user)
        },

        // Action to refresh access token
        refreshToken() {
            // Send request to refresh access token
            axios.post('/api/refresh/', {
                refresh: this.user.refresh
            })
                .then((response) => {
                    // Update access token
                    this.user.access = response.data.access

                    // Store access token in localStorage
                    localStorage.setItem('user.access', response.data.access)

                    // Set authorization header for future requests
                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch((error)=>{
                    // Log error and remove tokens if refresh fails
                    console.log(error)

                    this.removeToken()
                })
        },
    }
})
