<template>
    <body> 
            <div class="flex justify-center p-5 md:p-10 lg:p-20 h-full bg-[#BADFE7]">
                <div class="shadow-md w-full md:w-1/3 bg-[#C2EDCE] content-center text-center font-OpenSans">
                    <div class="pt-2 md:pt-4 text-sm md:text-base">
                        <h1 class="text-lg md:text-2xl font-bold">Sign Up</h1>

                        <p class="text-[#979797] text-center text-xs md:text-sm">
                            Already have an account? <RouterLink to="/login" class="underline">Click here</RouterLink> to login!
                        </p>
                    </div>
                </div>

                
                    <div class="shadow-md w-full md:w-1/2 p-14 bg-white font-OpenSans">
                        <form class="space-y-4 md:space-y-6 text-xs" v-on:submit.prevent="submitForm">
                            <div>
                                <label>Name</label><br>
                                <input type="name" placeholder="Your name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" v-model="form.name">
                            </div>

                            <div>
                                <label>E-mail</label><br>
                                <input type="email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" v-model="form.email">
                            </div>

                            <div>
                                <label>Password</label><br>
                                <input type="password" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" v-model="form.password1">
                            </div>

                            <div>
                                <label>Repeat Password</label><br>
                                <input type="password" placeholder="Repeat your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" v-model="form.password2">
                            </div>

                            <template v-if="errors.length > 0">
                                <div class="bg-red-300 text-white rounded-lg p-6">
                                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                                </div>
                            </template>
                            
                            <div>
                                <button class="py-2 px-6 rounded-full bg-[#BADFE7] hover:bg-sky-800 hover:text-white active:ring active:ring-sky-600">Sign Up</button>
                            </div>
                        </form>
                    </div>
                
            </div>
        
    </body>
</template>


<script>
    import axios from 'axios'
    import { useToastStore } from '@/stores/toast'

    export default {
        // Setup function to initialize toast store
        setup() {
            const toastStore = useToastStore()

            return {
                toastStore
            }
        },

        // Component data
        data() {
            return {
                // Form fields
                form: {
                    email: '',
                    name: '',
                    password1: '',
                    password2: ''
                },
                // Array to store validation errors
                errors: [],
            }
        },

        // Component methods
        methods: {
            // Method to submit signup form
            submitForm() {
                this.errors = []

                // Validate form fields
                if (this.form.email === '') {
                    this.errors.push('Your e-mail is missing')
                }

                if (this.form.name === '') {
                    this.errors.push('Your name is missing')
                }

                if (this.form.password1 === '') {
                    this.errors.push('Your password is missing')
                }

                if (this.form.password1 !== this.form.password2) {
                    this.errors.push('The password does not match')
                }

                // Submit form data if no errors
                if (this.errors.length === 0) {
                    axios
                        .post('http://localhost:8000/account/signup/', this.form)
                        .then(response => {
                            if (response.data.message === 'success') {
                                // Show success toast if signup is successful
                                this.toastStore.showToast(5000, 'The user is registered. Please proceed now to login page', 'bg-emerald-500')

                                // Log the form data to console
                                console.log('Email:', this.form.email)
                                console.log('Name:', this.form.name)
                                console.log('Password1:', this.form.password1)
                                console.log('Password2:', this.form.password2)

                                // Clear form fields
                                this.form.email = ''
                                this.form.name = ''
                                this.form.password1 = ''
                                this.form.password2 = ''
                            } else {
                                // Show error toast if something went wrong during signup
                                this.toastStore.showToast(5000, this.errors, 'bg-red-300')
                            }
                        })
                        .catch(error => {
                            console.log('error', error)
                        })
                }
            }
        }
    }
</script>