<template>
    <body> 
        <main class="px-8 py-6 bg-gray-100">
            <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
                <div class="main-left col-span-2">
                    <div class="p-12 bg-white border border-gray-200 rounded-lg">
                        <h1 class="mb-6 text-2xl">Sign Up</h1>

                        <p class="font-bold">
                            Already have an account? <RouterLink to="/login" class="underline">Click here</RouterLink> to login!
                        </p>
                    </div>
                </div>

                <div class="main-center col-span-2 space-y-4">
                    <div class="p-12 bg-white border border-gray-200 rounded-lg">
                        <form class="space-y-6" v-on:submit.prevent="submitForm">
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
                                <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign Up</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </main>
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
                    // Log the form data to the console
                    console.log('Form Data:', {
                        email: this.form.email,
                        name: this.form.name,
                        password1: this.form.password1
                    });

                    axios
                        .post('/api/signup/', this.form)
                        .then(response => {
                            if (response.data.message === 'success') {
                                // Show success toast if signup is successful
                                this.toastStore.showToast(5000, 'The user is registered. Please activate your account by clicking your email link.', 'bg-emerald-500')

                                // Clear form fields
                                this.form.email = ''
                                this.form.name = ''
                                this.form.password1 = ''
                                this.form.password2 = ''
                            } else {
                                // Show error toast if something went wrong during signup
                                this.toastStore.showToast(5000, 'Something went wrong. Please try again', 'bg-red-300')
                            }
                        })
                        .catch(error => {
                            console.log('error', error)
                        });
                }

            }
        }
    }
</script>