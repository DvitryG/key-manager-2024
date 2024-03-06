
function Editing (){
    return(
        <>
            <div className="container">
                <div className="form">
                    <form>
                        <label className="label_blo">ФИО</label>
                        <input className="w-100" type="text" placeholder="Last and First name" />
                    </form>
                    <form>
                        <label className="label_blo">Email</label>
                        <input className="w-100" type="email" placeholder="Your email" />
                    </form>
                    <form>
                        <label className="label_blo">Роли</label>
                        <div>
                            <form>
                                <input type="checkbox" id="student"  />
                                <label className="check" for="student">Студент</label>
                            </form>
                            <form>
                                <input type="checkbox" id="teach" />
                                <label className="check" for="teach">Преподаватель</label>
                            </form>
                            <form>
                                <input type="checkbox" id="dekan"/>
                                <label className="check" for="dekan">Деканат</label>
                            </form>
                            <form>
                                <input type="checkbox" id="admin" />
                                <label className="check" for="admin">Админ</label>
                            </form>
                        </div>

                    </form>
                    <input type="submit" value="Изменить"/>
                </div>

            </div>

        </>
    )

}

export default Editing;