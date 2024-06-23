<template>
    <div  class="flex justify-center p-5 md:p-10 lg:p-20 h-full bg-[#BADFE7]">
        
            <div class="shadow-md w-full md:w-1/3 bg-[#C2EDCE] content-center text-center font-OpenSans">
                <h1 class="text-lg md:text-2xl font-bold">Log in</h1>


                <p class="text-[#979797] text-center text-xs md:text-sm">
                    Don't have an account? <RouterLink :to="{'name': 'signup'}" class="underline">Click here</RouterLink> to create one!
                </p>
            </div>
        

        
            <div class="shadow-md w-full md:w-1/2 p-14 bg-white font-OpenSans">
                <form class="space-y-4 md:space-y-6 text-xs" v-on:submit.prevent="submitForm">
                    <div>
                        <label class="font-bold">E-mail</label><br>
                        <input type="email" v-model="form.email" placeholder="Your e-mail address" class="w-full mt-2 p-3 md:p-4 border border-[#979797] rounded-lg">
                    </div>

                    <div>
                        <label class="font-bold">Password</label><br>
                        <input type="password" v-model="form.password" placeholder="Your password" class="w-full mt-2 p-3 md:p-4 border border-[#979797] rounded-lg">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div class="pt-4 md:pt-8 flex justify-center">
                        <button class="py-2 px-6 rounded-full bg-[#BADFE7] hover:bg-sky-800 hover:text-white active:ring active:ring-sky-600">Log in</button>
                    </div>
                </form>
            </div>
        
    </div>
</template>

<script>
import axios from 'axios'

import { useUserStore } from '@/stores/user'

export default {
    // Setup function to initialize user store
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    // Component data
    data() {
        return {
            // Form fields for email and password
            form: {
                email: '',
                password: '',
            },
            // Array to store form validation errors
            errors: []
        }
    },
    // Component methods
    methods: {
        // Method to handle form submission
        async submitForm() {
            // Clear previous errors
            this.errors = []

            // Check if email is missing
            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            // Check if password is missing
            if (this.form.password === '') {
                this.errors.push('Your password is missing')
            }

            // If no errors, proceed with form submission
            if (this.errors.length === 0) {
                // Attempt to login
                await axios
                    .post('http://localhost:8000/account/login/', this.form)
                    .then(response => {
                        // Set access and refresh tokens in user store
                        this.userStore.setToken(response.data)

                        // Set authorization header for future requests
                        axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                    })
                    .catch(error => {
                        // Log error and display error message
                        console.log('error', error)
                        this.errors.push('The email or password is incorrect!')
                    })
            }
            
            // If no errors, fetch user information
            if (this.errors.length === 0) {
                await axios
                    .get('http://localhost:8000/account/me/')
                    .then(response => {
                        // Set user information in user store
                        this.userStore.setUserInfo(response.data)

                        // Redirect to feed page
                        this.$router.push('/entercode')
                    })
                    .catch(error => {
                        // Log error if user information fetch fails
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>