package nl.tudelft.jpacman.level;

import nl.tudelft.jpacman.sprite.PacManSprites;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class PlayerTest {
    /*
     * - Create a PacManSprites object => Pass to a PlayerFactory constructor => Instantiate a Player
     */
    // Instantiations
    private static final PacManSprites pms = new PacManSprites();
    private final PlayerFactory factory = new PlayerFactory(pms);
    private final Player thePlayer = factory.createPacMan();

    // Method
    @Test
    void testAlive(){
        assertThat(thePlayer.isAlive()).isEqualTo(true);
    }
}
