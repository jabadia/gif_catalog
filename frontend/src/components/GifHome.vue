<template>
    <div>
        <div class="row mb-4">
            <div class="col-12">
                <button @click="reloadPics" class="btn btn-primary">show others...</button>
            </div>
        </div>
        <div class="row">
            <gif-pic v-for="pic in pics" :key="pic.id" :pic="pic"></gif-pic>
        </div>
    </div>
</template>

<script>
    import gifPicsApi from '../services/gifPicsApi.js';
    import GifPic from './GifPic.vue';

    export default {
        data() {
            return {
                pics: [],
            };
        },
        methods: {
            reloadPics() {
                gifPicsApi.getRandomPics().then(pics => {
                    this.pics = pics;
                });
            }
        },
        mounted() {
            this.reloadPics();
        },
        components: {
            GifPic,
        },
    };
</script>

<style lang="less" rel="stylesheet/less">
</style>
