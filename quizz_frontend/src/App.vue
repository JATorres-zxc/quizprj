<template>
    <nav class="py-10 px-8 border-b border-gray-200">
        <div class="max-w-7xl mx-auto">
            <div class="flex items-center justify-between">
                <div class="menu-left">
                    <a href="#" class="text-xl">QuizIt</a>
                </div>

                <!-- redirecting code search icon -->
                <div class="flex justify-center items-center">
                    <button @click="goToPage" class="bg-purple-900 text-white px-4 py-2 rounded-lg">
                        Enter Code Here
                    </button>
                </div>

                <!-- search quiz button -->
                <div class="bg-white border border-gray-200 rounded-lg">
                    <form v-on:submit.prevent="submitForm" class="p-4 flex space-x-4">  
                        <input v-model="query" type="search" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What are you looking for?">

                        <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                            </svg>      
                        </button>
                    </form>
                </div>
                

                <!-- <div class="menu-right">
                    <template v-if="userStore.user.isAuthenticated && userStore.user.id">
                        <RouterLink :to="{name: 'profile', params:{'id': userStore.user.id}}">
                            <img :src="userStore.user.avatar" class="w-12 rounded-full">
                        </RouterLink>
                    </template>

                    <template v-else>
                        <RouterLink to="/login" class="mr-4 py-4 px-6 bg-gray-600 text-white rounded-lg">Log in</RouterLink>
                        <RouterLink to="/signup" class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign up</RouterLink>
                    </template>
                </div> -->

                <!-- <div class="menu-right">
                    <button class="mr-4 py-4 px-6 bg-gray-600 text-white rounded-lg">Log in</button>
                    <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign up</button>
                </div> -->

                <div class="menu-right">
                    <router-link to="/login" class="mr-4 py-4 px-6 bg-gray-600 text-white rounded-lg">LogIn</router-link>
                    <router-link to="/signup" class="py-4 px-6 bg-purple-600 text-white rounded-lg">SignUp</router-link>
                </div>

            </div>
        </div>
    </nav>

    <main class="px-8 py-6 bg-gray-100">
        <RouterView />
    </main>

</template>


<script setup>
</script>


<style scoped>
</style>
