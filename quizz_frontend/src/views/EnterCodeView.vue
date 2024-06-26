<template>
    <div class="min-h-screen flex flex-col items-center justify-between bg-gray-100 p-4">
    <!-- Title -->
        <h1 class="text-4xl font-bold mt-10">QuizIt</h1>
        
        <!-- Form -->
        <div class="flex-grow flex items-center justify-center">
            <form class="bg-white rounded-lg shadow-lg p-8 flex items-center space-x-4">
            <label for="code" class="block text-xl font-medium text-gray-700 mb-2">Enter Code</label>
            <input
                type="text"
                id="code"
                name="code"
                placeholder="Enter code"
                class="block w-64 px-4 py-2 rounded-lg border border-gray-300 focus:ring focus:ring-blue-200 focus:outline-none"
            />
            <button
                type="submit"
                class="px-4 py-2 bg-blue-500 text-white rounded-lg shadow hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-200"
            >
                Join
            </button>
            </form>
        </div>
        
        <!-- Bottom Containers -->
        <div class="flex justify-around w-full max-w-4xl mb-10">
            <a href="#" class="flex flex-col items-center bg-white rounded-lg shadow-lg p-4 hover:shadow-xl transition-shadow">
            <img src="https://via.placeholder.com/150" alt="Placeholder" class="rounded-full mb-4">
            <h2 class="text-lg font-semibold">Title 1</h2>
            </a>
            <a href="#" class="flex flex-col items-center bg-white rounded-lg shadow-lg p-4 mx-4 hover:shadow-xl transition-shadow">
            <img src="https://via.placeholder.com/150" alt="Placeholder" class="rounded-full mb-4">
            <h2 class="text-lg font-semibold">Title 2</h2>
            </a>
            <a href="#" class="flex flex-col items-center bg-white rounded-lg shadow-lg p-4 hover:shadow-xl transition-shadow">
            <img src="https://via.placeholder.com/150" alt="Placeholder" class="rounded-full mb-4">
            <h2 class="text-lg font-semibold">Title 3</h2>
            </a>
        </div>
    </div>
</template>


<script>
import axios from 'axios'

import { useUserStore } from '../stores/user' // Adjust the path based on your project structure

export default {
    name: 'EnterCodeView', // Replace with your actual component name

    setup() {
        const userStore = useUserStore();

        // Initialize store on component mount
        userStore.initStore();

        // Set Axios headers if user is authenticated
        if (userStore.user.isAuthenticated) {
            axios.defaults.headers.common["Authorization"] = "Bearer " + userStore.user.access;
        }
    }
}
</script>