<template>
    <div class="min-h-screen flex flex-col items-center bg-gray-100 p-6">
    <!-- Top Controls -->
    <div class="w-full max-w-5xl flex items-center justify-between mb-4 p-4 bg-white shadow-lg rounded-lg">
        <div class="flex items-center space-x-4">
        <button class="flex items-center space-x-2 px-4 py-2 bg-gray-200 rounded-lg">
            <span>Multiple Choice</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M5.293 9.293a1 1 0 011.414 0L10 12.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
        </button>
        <div class="flex items-center space-x-2">
            <button class="px-4 py-2 bg-gray-200 rounded-lg">A</button>
            <button class="px-4 py-2 bg-gray-200 rounded-lg">B</button>
            <button class="px-4 py-2 bg-gray-200 rounded-lg">I</button>
            <button class="px-4 py-2 bg-gray-200 rounded-lg">U</button>
            <button class="px-4 py-2 bg-gray-200 rounded-lg">S</button>
            <button class="px-4 py-2 bg-gray-200 rounded-lg">X</button>
        </div>
        </div>
        <button class="px-4 py-2 bg-purple-500 text-white rounded-lg">Save question</button>
        <button class="px-4 py-2 bg-red-500 text-white rounded-lg">Delete question</button>
        <button class="px-4 py-2 bg-green-500 text-white rounded-lg">Edit</button>
    </div>

    <!-- Question and Answers Section -->
    <div class="w-full max-w-5xl bg-white shadow-lg rounded-lg p-6">
        <!-- Question Area -->
        <div class="mb-6 p-4 bg-purple-900 text-white rounded-lg">
        <p class="text-xl">Type question here</p>
        </div>

        <!-- Answer Options -->
        <div class="grid grid-cols-4 gap-4">
        <div class="flex flex-col items-center p-4 bg-blue-600 text-white rounded-lg">
            <p>Type answer option here</p>
            <button class="mt-2 bg-gray-200 p-1 rounded-lg">Delete</button>
        </div>
        <div class="flex flex-col items-center p-4 bg-teal-600 text-white rounded-lg">
            <p>Type answer option here</p>
            <button class="mt-2 bg-gray-200 p-1 rounded-lg">Delete</button>
        </div>
        <div class="flex flex-col items-center p-4 bg-yellow-600 text-white rounded-lg">
            <p>Type answer option here</p>
            <button class="mt-2 bg-gray-200 p-1 rounded-lg">Delete</button>
        </div>
        <div class="flex flex-col items-center p-4 bg-pink-600 text-white rounded-lg">
            <p>Type answer option here</p>
            <button class="mt-2 bg-gray-200 p-1 rounded-lg">Delete</button>
        </div>
        </div>

        <!-- Answer Type Buttons -->
        <div class="mt-6 flex justify-center space-x-4">
        <button class="px-4 py-2 bg-gray-200 rounded-lg">Single correct answer</button>
        <button class="px-4 py-2 bg-gray-200 rounded-lg">Multiple correct answers</button>
        </div>
    </div>
    </div>
</template>

<script>
export default {
    name: 'QuizEditor',
};
</script>

<style scoped>
/* Add any custom styles here if needed */
</style>
