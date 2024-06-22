<template>
    <div class="min-h-screen flex flex-col items-center bg-gray-100 p-6">
    <!-- Header Section -->
    <div class="w-full max-w-4xl">
        <h1 class="text-2xl font-semibold mb-2">Create a new study set</h1>
        <p class="text-sm text-gray-600 mb-4">Saved under 1 min ago</p>
    </div>

    <!-- Form Section -->
    <div class="w-full max-w-4xl bg-white rounded-lg shadow-lg p-6 mb-6">
        <div class="flex flex-col space-y-4 mb-6">
        <input type="text" placeholder='Enter a title, like "Biology - Chapter 22: Evolution"' class="w-full p-3 border border-gray-300 rounded-lg" />
        <textarea placeholder="Add a description..." class="w-full p-3 border border-gray-300 rounded-lg"></textarea>
        <div class="flex space-x-4">
            <input type="text" placeholder="School name" class="w-1/2 p-3 border border-gray-300 rounded-lg" />
            <input type="text" placeholder="Course" class="w-1/2 p-3 border border-gray-300 rounded-lg" />
        </div>
        </div>

        <div class="flex space-x-4 mb-6">
        <button class="bg-gray-200 text-gray-700 px-4 py-2 rounded-lg">+ Import</button>
        <button class="bg-gray-200 text-gray-700 px-4 py-2 rounded-lg">+ Add diagram</button>
        <button class="bg-gray-200 text-gray-700 px-4 py-2 rounded-lg">Create from notes</button>
        </div>

        <!-- Terms Section -->
        <div class="space-y-4">
        <div class="flex items-center justify-between p-4 border border-gray-300 rounded-lg">
            <div class="flex space-x-4 w-full">
            <input type="text" placeholder="Enter term" class="w-1/2 p-2 border border-gray-300 rounded-lg" />
            <input type="text" placeholder="Enter definition" class="w-1/2 p-2 border border-gray-300 rounded-lg" />
            </div>
            <button class="bg-gray-200 text-gray-700 px-4 py-2 rounded-lg">IMAGE</button>
        </div>

        <div class="flex items-center justify-between p-4 border border-gray-300 rounded-lg">
            <div class="flex space-x-4 w-full">
            <input type="text" placeholder="Enter term" class="w-1/2 p-2 border border-gray-300 rounded-lg" />
            <input type="text" placeholder="Enter definition" class="w-1/2 p-2 border border-gray-300 rounded-lg" />
            </div>
            <button class="bg-gray-200 text-gray-700 px-4 py-2 rounded-lg">IMAGE</button>
        </div>

        <div class="text-center">
            <button class="bg-gray-200 text-gray-700 px-4 py-2 rounded-lg">+ ADD CARD</button>
        </div>
        </div>
    </div>

    <!-- Footer Buttons -->
    <div class="w-full max-w-4xl flex justify-end space-x-4">
        <button class="bg-gray-200 text-gray-700 px-4 py-2 rounded-lg">Create</button>
        <button class="bg-blue-500 text-white px-4 py-2 rounded-lg">Create and practice</button>
    </div>
    </div>
</template>

<script>
export default {
    name: 'StudySetView',
};
</script>

<style scoped>
/* Add any custom styles here if needed */
</style>
