<template>
    <div class="col-4 mb-4">
        <div class="card" style="height: 100%;">
            <img :src="pic.gifurl" :alt="pic.title" class="card-img-top"
                 style="height: 200px; object-fit: cover; background: #ddd;">
            <div class="card-body d-flex flex-column align-items-start">
                <h4 class="card-title">{{ pic.title }}</h4>
                <p class="card-text" style="flex-grow: 1"></p>
                <a href="#" class="btn btn-primary align-self-end">Go</a>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['pic'],
        data() {
            return {};
        },
    };
</script>

<style lang="less" rel="stylesheet/less">
</style>
