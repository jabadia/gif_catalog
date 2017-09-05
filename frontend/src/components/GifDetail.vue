<template>
    <div class="row">
        <div class="col-12">
            <h1>{{ pic.title }}</h1>
        </div>
        <div class="col-12">
            <router-link to="/">go back</router-link>
        </div>
        <div class="col-12">
            <img class="img-fluid w-100" :src="pic.gifurl" alt="">
        </div>
    </div>
</template>

<script>
    import gifPicsApi from "../services/gifPicsApi";

    export default {
        props: ['id'],
        data() {
            return {
                pic: {},
            };
        },
        methods: {
            fetchData() {
                gifPicsApi.getDetail(this.id).then(detail => {
                    this.pic = detail;
                });
            }
        },
        watch: {
            '$route': 'fetchData',
        },
        created() {
            this.fetchData();
        }
    };
</script>

<style lang="less" rel="stylesheet/less">
</style>
