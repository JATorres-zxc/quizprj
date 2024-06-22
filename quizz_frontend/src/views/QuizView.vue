<template>
    <div class="min-h-screen flex flex-col items-center bg-gray-100 p-4">
    <!-- Top Horizontal Div -->
    <div class="w-full flex items-center justify-between bg-white p-4 shadow-md mb-4">
        <!-- Settings Button -->
        <button @click="handleSettings" class="flex items-center justify-center bg-gray-200 hover:bg-gray-300 rounded-full p-2">
        <svg class="w-6 h-6 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 3v2a1 1 0 001 1h2a1 1 0 001-1V3m0 0h2a1 1 0 011 1v2a1 1 0 011 1v2a1 1 0 01-1 1h-2a1 1 0 01-1 1h-2a1 1 0 01-1-1H9a1 1 0 01-1-1V6a1 1 0 011-1h2a1 1 0 001-1V3z"></path>
        </svg>
        </button>
        <!-- Music Toggle Button -->
        <button @click="toggleMusic" class="flex items-center space-x-3 bg-gray-200 hover:bg-gray-300 rounded-full p-2">
        <span class="text-gray-700">Music</span>
        <input type="checkbox" class="form-checkbox h-5 w-5 text-blue-600" :checked="isMusicOn" readonly>
        </button>
        <!-- Score Button -->
        <button @click="showScore" class="text-gray-700 font-semibold bg-gray-200 hover:bg-gray-300 rounded-full p-2">
        Score: 10
        </button>
        <!-- Status Bar Button -->
        <button @click="showStatus" class="text-gray-700 bg-gray-200 hover:bg-gray-300 rounded-full p-2">
        Questions Left: 5
        </button>
    </div>

    <!-- Main Question Div -->
    <div class="w-full bg-white rounded-lg shadow-lg p-8">
        <!-- Question -->
        <h2 class="text-2xl font-semibold mb-6">What is the capital of France?</h2>
        <!-- Choices -->
        <div class="space-y-4">
        <div class="p-4 bg-blue-100 rounded-lg shadow-md cursor-pointer hover:bg-blue-200">
            A. Paris
        </div>
        <div class="p-4 bg-blue-100 rounded-lg shadow-md cursor-pointer hover:bg-blue-200">
            B. Madrid
        </div>
        <div class="p-4 bg-blue-100 rounded-lg shadow-md cursor-pointer hover:bg-blue-200">
            C. Rome
        </div>
        </div>
    </div>
    </div>
</template>

<script>
export default {
    name: 'QuizView',
    data() {
    return {
        isMusicOn: false,
    };
    },
    methods: {
    handleSettings() {
        // Handle settings click
        console.log('Settings clicked');
    },
    toggleMusic() {
        // Toggle music on/off
        this.isMusicOn = !this.isMusicOn;
        console.log('Music toggled:', this.isMusicOn);
    },
    showScore() {
        // Show score
        console.log('Score button clicked');
    },
    showStatus() {
        // Show status bar
        console.log('Status bar clicked');
    },
    },
};
</script>