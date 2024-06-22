<template>
    <div class="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
    <!-- Main Flip Div -->
    <div class="relative w-full max-w-2xl mb-8">
        <div class="w-full h-96 flex items-center justify-center bg-white rounded-lg shadow-lg p-8 cursor-pointer"
            @click="flipCard">
        <div v-if="!isFlipped" class="text-3xl font-semibold">
            Front Side Text
        </div>
        <div v-else class="text-3xl font-semibold">
            Back Side Text
        </div>
        </div>
        
        <!-- Navigation Arrows -->
        <div class="flex justify-between mt-4">
        <button @click="previousCard" class="bg-blue-500 text-white rounded-full p-4 hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
            </svg>
        </button>
        <button @click="nextCard" class="bg-blue-500 text-white rounded-full p-4 hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
            </svg>
        </button>
        </div>
    </div>
    </div>
</template>

<script>
export default {
    name: 'FlashcardView',
    data() {
    return {
        isFlipped: false,
    };
    },
    methods: {
    flipCard() {
        this.isFlipped = !this.isFlipped;
    },
    previousCard() {
        // Handle previous card logic
        console.log('Previous card');
    },
    nextCard() {
        // Handle next card logic
        console.log('Next card');
    },
    },
};
</script>

<style scoped>
/* Add any custom styles here if needed */
</style>
