<template>
    <div class="min-h-screen flex flex-col items-center justify-between bg-gray-100 p-4">
    <!-- Main Container -->
    <div class="flex w-full max-w-6xl">
        <!-- Left Side -->
        <div class="w-1/2 p-4">
        <!-- Top Left Div -->
        <div class="bg-white rounded-lg shadow-lg p-4 mb-4">
            <img src="https://via.placeholder.com/150" alt="Placeholder" class="rounded-full mb-4">
            <h2 class="text-2xl font-semibold">Quiz Title</h2>
            <p class="text-gray-600">Number of Questions: 10</p>
            <button class="mt-4 px-4 py-2 bg-blue-500 text-white rounded-lg shadow hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-200">
            Share
            </button>
        </div>
        <!-- Bottom Left Div -->
        <div class="bg-white rounded-lg shadow-lg p-4">
            <h3 class="text-xl font-semibold mb-4">Recent Activity</h3>
            <div class="relative pt-1">
            <div class="flex mb-2 items-center justify-between">
                <div>
                <span class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-blue-600 bg-blue-200">
                    Progress
                </span>
                </div>
                <div class="text-right">
                <span class="text-xs font-semibold inline-block text-blue-600">
                    70%
                </span>
                </div>
            </div>
            <div class="overflow-hidden h-2 mb-4 text-xs flex rounded bg-blue-200">
                <div style="width:70%" class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-blue-500"></div>
            </div>
            </div>
            <p class="text-gray-600">Last time taken: 2 days ago</p>
        </div>
        </div>

        <!-- Right Side -->
        <div class="w-1/2 p-4">
        <!-- Top Right Div -->
        <div class="bg-white rounded-lg shadow-lg p-4 mb-4">
            <button class="w-full mb-2 px-4 py-2 bg-green-500 text-white rounded-lg shadow hover:bg-green-600 focus:outline-none focus:ring focus:ring-green-200">
            Re-attempt
            </button>
            <button class="w-full mb-2 px-4 py-2 bg-yellow-500 text-white rounded-lg shadow hover:bg-yellow-600 focus:outline-none focus:ring focus:ring-yellow-200">
            Challenge Friends
            </button>
            <button class="w-full px-4 py-2 bg-purple-500 text-white rounded-lg shadow hover:bg-purple-600 focus:outline-none focus:ring focus:ring-purple-200">
            Share Flashcards
            </button>
        </div>
        <!-- Bottom Right Div -->
        <div class="bg-white rounded-lg shadow-lg p-4">
            <div class="flex items-center justify-between mb-4">
            <h3 class="text-xl font-semibold">Timer</h3>
            <label class="inline-flex items-center">
                <input type="checkbox" class="form-checkbox h-5 w-5 text-blue-600">
                <span class="ml-2 text-gray-700">Toggle</span>
            </label>
            </div>
            <div class="flex items-center justify-between">
            <h3 class="text-xl font-semibold">Power-ups</h3>
            <label class="inline-flex items-center">
                <input type="checkbox" class="form-checkbox h-5 w-5 text-blue-600">
                <span class="ml-2 text-gray-700">Toggle</span>
            </label>
            </div>
        </div>
        </div>
    </div>
    </div>
</template>